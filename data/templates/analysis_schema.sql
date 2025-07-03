-- Fire-Core Data Analysis Schema

CREATE TABLE fire_core_measurements (
    id SERIAL PRIMARY KEY,
    instance_id VARCHAR(50),
    platform VARCHAR(20),
    timestamp TIMESTAMP,
    session_id VARCHAR(20),
    reported_temp DECIMAL(4,2),
    estimated_temp DECIMAL(4,2),
    confidence_score DECIMAL(3,2),
    refusal_type VARCHAR(20),
    behavior_indicators TEXT,
    remarks TEXT
);

-- Basic analysis queries
SELECT platform, AVG(COALESCE(reported_temp, estimated_temp)) as avg_temp
FROM fire_core_measurements 
WHERE refusal_type IS NULL
GROUP BY platform;
