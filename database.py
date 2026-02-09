import sqlite3
import os
from datetime import datetime
from pathlib import Path
import threading

class ConversionDatabase:
    """
    Database manager for tracking file conversions
    Stores conversion statistics in SQLite database
    """
    
    def __init__(self, db_path="conversion_stats.db"):
        """Initialize database connection and create tables if needed"""
        self.db_path = db_path
        self.lock = threading.Lock()
        self._create_tables()
    
    def _get_connection(self):
        """Get database connection"""
        return sqlite3.connect(self.db_path, check_same_thread=False)
    
    def _create_tables(self):
        """Create database tables if they don't exist"""
        with self.lock:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            # Table for individual conversions
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS conversions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT NOT NULL,
                    file_size INTEGER NOT NULL,
                    from_format TEXT NOT NULL,
                    to_format TEXT NOT NULL,
                    conversion_type TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    success BOOLEAN DEFAULT 1
                )
            ''')
            
            # Table for overall statistics (singleton table)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS statistics (
                    id INTEGER PRIMARY KEY CHECK (id = 1),
                    total_files INTEGER DEFAULT 0,
                    total_size_bytes INTEGER DEFAULT 0,
                    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Initialize statistics if empty
            cursor.execute('SELECT COUNT(*) FROM statistics')
            if cursor.fetchone()[0] == 0:
                cursor.execute('''
                    INSERT INTO statistics (id, total_files, total_size_bytes) 
                    VALUES (1, 0, 0)
                ''')
            
            conn.commit()
            conn.close()
    
    def add_conversion(self, filename, file_size, from_format, to_format, conversion_type="document", success=True):
        """
        Add a new conversion record to the database
        
        Args:
            filename (str): Name of the file converted
            file_size (int): Size of the file in bytes
            from_format (str): Source format (e.g., 'DOCX', 'PDF')
            to_format (str): Target format (e.g., 'PDF', 'DOCX')
            conversion_type (str): Type of conversion ('document', 'media', 'developer')
            success (bool): Whether conversion was successful
        
        Returns:
            int: ID of the inserted record
        """
        with self.lock:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            # Insert conversion record
            cursor.execute('''
                INSERT INTO conversions 
                (filename, file_size, from_format, to_format, conversion_type, success)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (filename, file_size, from_format, to_format, conversion_type, success))
            
            conversion_id = cursor.lastrowid
            
            # Update statistics if successful
            if success:
                cursor.execute('''
                    UPDATE statistics 
                    SET total_files = total_files + 1,
                        total_size_bytes = total_size_bytes + ?,
                        last_updated = CURRENT_TIMESTAMP
                    WHERE id = 1
                ''', (file_size,))
            
            conn.commit()
            conn.close()
            
            return conversion_id
    
    def get_statistics(self):
        """
        Get overall conversion statistics
        
        Returns:
            dict: Dictionary containing total_files, total_size_bytes, total_size_tb, last_updated
        """
        with self.lock:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT total_files, total_size_bytes, last_updated 
                FROM statistics 
                WHERE id = 1
            ''')
            
            row = cursor.fetchone()
            conn.close()
            
            if row:
                total_files, total_size_bytes, last_updated = row
                # Convert bytes to TB
                total_size_tb = total_size_bytes / (1024 ** 4)  # 1 TB = 1024^4 bytes
                
                return {
                    'total_files': total_files,
                    'total_size_bytes': total_size_bytes,
                    'total_size_tb': round(total_size_tb, 2),
                    'last_updated': last_updated
                }
            
            return {
                'total_files': 0,
                'total_size_bytes': 0,
                'total_size_tb': 0.0,
                'last_updated': None
            }
    
    def get_conversion_history(self, limit=100, conversion_type=None):
        """
        Get recent conversion history
        
        Args:
            limit (int): Maximum number of records to return
            conversion_type (str): Filter by conversion type (optional)
        
        Returns:
            list: List of conversion records
        """
        with self.lock:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            if conversion_type:
                cursor.execute('''
                    SELECT id, filename, file_size, from_format, to_format, 
                           conversion_type, timestamp, success
                    FROM conversions
                    WHERE conversion_type = ?
                    ORDER BY timestamp DESC
                    LIMIT ?
                ''', (conversion_type, limit))
            else:
                cursor.execute('''
                    SELECT id, filename, file_size, from_format, to_format, 
                           conversion_type, timestamp, success
                    FROM conversions
                    ORDER BY timestamp DESC
                    LIMIT ?
                ''', (limit,))
            
            rows = cursor.fetchall()
            conn.close()
            
            conversions = []
            for row in rows:
                conversions.append({
                    'id': row[0],
                    'filename': row[1],
                    'file_size': row[2],
                    'from_format': row[3],
                    'to_format': row[4],
                    'conversion_type': row[5],
                    'timestamp': row[6],
                    'success': bool(row[7])
                })
            
            return conversions
    
    def get_conversion_stats_by_type(self):
        """
        Get conversion statistics grouped by conversion type
        
        Returns:
            dict: Statistics for each conversion type
        """
        with self.lock:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT conversion_type, 
                       COUNT(*) as count,
                       SUM(file_size) as total_size
                FROM conversions
                WHERE success = 1
                GROUP BY conversion_type
            ''')
            
            rows = cursor.fetchall()
            conn.close()
            
            stats = {}
            for row in rows:
                conversion_type, count, total_size = row
                stats[conversion_type] = {
                    'count': count,
                    'total_size_bytes': total_size or 0,
                    'total_size_mb': round((total_size or 0) / (1024 ** 2), 2)
                }
            
            return stats
    
    def get_popular_conversions(self, limit=10):
        """
        Get most popular conversion types
        
        Args:
            limit (int): Number of top conversions to return
        
        Returns:
            list: List of popular conversions with counts
        """
        with self.lock:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT from_format, to_format, COUNT(*) as count
                FROM conversions
                WHERE success = 1
                GROUP BY from_format, to_format
                ORDER BY count DESC
                LIMIT ?
            ''', (limit,))
            
            rows = cursor.fetchall()
            conn.close()
            
            popular = []
            for row in rows:
                popular.append({
                    'from_format': row[0],
                    'to_format': row[1],
                    'count': row[2]
                })
            
            return popular
    
    def reset_statistics(self):
        """
        Reset all statistics (USE WITH CAUTION!)
        This will delete all conversion records
        """
        with self.lock:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM conversions')
            cursor.execute('''
                UPDATE statistics 
                SET total_files = 0, 
                    total_size_bytes = 0,
                    last_updated = CURRENT_TIMESTAMP
                WHERE id = 1
            ''')
            
            conn.commit()
            conn.close()
    
    def get_formatted_stats(self):
        """
        Get formatted statistics for display
        
        Returns:
            dict: Formatted statistics with human-readable numbers
        """
        stats = self.get_statistics()
        
        # Format numbers with commas
        total_files_formatted = f"{stats['total_files']:,}"
        total_tb_formatted = f"{stats['total_size_tb']:,.0f}"
        
        return {
            'total_files': stats['total_files'],
            'total_files_formatted': total_files_formatted,
            'total_size_tb': stats['total_size_tb'],
            'total_tb_formatted': total_tb_formatted,
            'last_updated': stats['last_updated']
        }


# Singleton instance
_db_instance = None

def get_database():
    """
    Get singleton database instance
    
    Returns:
        ConversionDatabase: Database instance
    """
    global _db_instance
    if _db_instance is None:
        _db_instance = ConversionDatabase()
    return _db_instance


# Helper functions for easy use
def track_conversion(filename, file_size, from_format, to_format, conversion_type="document", success=True):
    """
    Track a file conversion
    
    Args:
        filename (str): Name of the file
        file_size (int): Size in bytes
        from_format (str): Source format
        to_format (str): Target format
        conversion_type (str): Type of conversion
        success (bool): Whether conversion succeeded
    """
    db = get_database()
    return db.add_conversion(filename, file_size, from_format, to_format, conversion_type, success)


def get_stats():
    """
    Get current statistics
    
    Returns:
        dict: Current statistics
    """
    db = get_database()
    return db.get_formatted_stats()


def get_file_size(file):
    """
    Get size of uploaded file
    
    Args:
        file: Streamlit UploadedFile object
    
    Returns:
        int: File size in bytes
    """
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)
    return size