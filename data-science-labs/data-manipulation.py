import json
from collections import defaultdict

def parse_dirty_logs(log_data):
    """
    Simulates Pandas .value_counts() and .groupby() functionality 
    using only pure Python dictionaries and exception handling.
    """
    error_counts = defaultdict(int)
    critical_users = set()
    
    for line_number, raw_line in enumerate(log_data, start=1):
        # 1. Handle Missing/Empty Data (Simulating dropna)
        if not raw_line.strip():
            continue
            
        # 2. Safely parse JSON, catching formatting errors
        try:
            log_entry = json.loads(raw_line)
        except json.JSONDecodeError:
            print(f"Warning: Malformed JSON on line {line_number}. Skipping.")
            continue
            
        # 3. Extract data safely using .get() to handle missing keys
        status_code = log_entry.get("status", "UNKNOWN")
        user_id = log_entry.get("user_id", "ANONYMOUS")
        
        # 4. Aggregate data (Simulating groupby / value_counts)
        error_counts[status_code] += 1
        
        # 5. Business Logic: Track users experiencing 500-level errors
        if isinstance(status_code, int) and 500 <= status_code < 600:
            critical_users.add(user_id)
            
    return dict(error_counts), list(critical_users)

if __name__ == "__main__":
    # Simulated dirty server logs (missing keys, bad JSON, empty lines)
    mock_log_file = [
        '{"timestamp": "2023-10-01T10:00:00", "status": 200, "user_id": "U123"}',
        '{"timestamp": "2023-10-01T10:01:00", "status": 404, "user_id": "U456"}',
        '', # Empty line
        '{"timestamp": "2023-10-01T10:02:00", "status": 500, "user_id": "U123"}',
        '{"timestamp": "2023-10-01T10:03:00", status: 200} ', # Bad JSON (missing quotes)
        '{"timestamp": "2023-10-01T10:04:00", "user_id": "U789"}', # Missing status key
        '{"timestamp": "2023-10-01T10:05:00", "status": 502, "user_id": "U999"}'
    ]
    
    counts, affected_users = parse_dirty_logs(mock_log_file)
    
    print("--- Log Analysis Results ---")
    print("\nStatus Code Counts:")
    for code, count in sorted(counts.items()):
        print(f"HTTP {code}: {count} occurrences")
        
    print(f"\nUsers affected by critical (5xx) errors: {affected_users}")
