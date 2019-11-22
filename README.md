```mysql
DROP PROCEDURE IF EXISTS cursorProc;
DELIMITER $$
CREATE PROCEDURE cursorProc( 
	IN start DATE,
	IN end DATE
)
BEGIN	
	DECLARE start_date DATE;
	DECLARE is_recurring CHAR(1);
	DECLARE recurring_type CHAR(10);
	DECLARE separation_count INT(3);

	DECLARE endOfRow BOOLEAN DEFAULT FALSE;
	
	DECLARE userCursor CURSOR FOR
		SELECT start_date, is_recurring, recurring_type, separation_count 
		FROM event LEFT JOIN recurring_pattern 
		ON event.parent_pattern_id = recurring_pattern.pattern_id
		WHERE start_date >= start AND start_date <= end;
	DECLARE CONTINUE HANDLER 
		FOR NOT FOUND SET endOfRow = TRUE;
	OPEN userCursor;

	cursor_loop: LOOP
		FETCH userCursor INTO start_date, is_recurring, recurring_type, separation_count;	
		
		IF endOfRow THEN
			LEAVE cursor_loop;
		ELSE
			CASE
				WHEN( is_recurring = "Y" ) THEN
					WHILE( start_date <= start ) DO
						CASE
							WHEN( recurring_type = "daily" ) THEN
								SET start_date = ADDDATE( start_date, INTERVAL 7 DAY );
							WHEN( recurring_type = "monthly" ) THEN
								SET start_date = ADDDATE( start_date, INTERVAL 1 MONTH );
						END CASE;
					END WHILE;
				WHEN( is_recurring = "N" ) THEN 
					SELECT id, event_title, event_description,
                    start_date, end_date, start_time, end_time, is_full_day_even
					FROM event LEFT JOIN recurring_pattern
					ON event.parent_pattern_id = recurring_pattern.pattern_id
					WHERE start_date >= start AND start_date <= end;
			END CASE;
		END IF;
	END LOOP cursor_loop;	
	CLOSE userCursor;
END $$
DELIMITER;
```
