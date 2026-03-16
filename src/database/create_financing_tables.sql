-- BUYERS TABLE
CREATE TABLE IF NOT EXISTS buyers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    credit_score INTEGER,
    monthly_income INTEGER,
    city TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- VEHICLE INVENTORY
CREATE TABLE IF NOT EXISTS vehicles (
    id SERIAL PRIMARY KEY,
    make TEXT,
    model TEXT,
    year INTEGER,
    price INTEGER,
    mileage INTEGER,
    dealer TEXT,
    city TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- FINANCING APPLICATIONS
CREATE TABLE IF NOT EXISTS financing_applications (
    id SERIAL PRIMARY KEY,
    buyer_id INTEGER REFERENCES buyers(id),
    vehicle_id INTEGER REFERENCES vehicles(id),
    down_payment INTEGER,
    loan_amount INTEGER,
    interest_rate FLOAT,
    loan_term INTEGER,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- LOAN DECISIONS
CREATE TABLE IF NOT EXISTS loan_decisions (
    id SERIAL PRIMARY KEY,
    application_id INTEGER REFERENCES financing_applications(id),
    decision TEXT,
    approved_amount INTEGER,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- AI AGENT LOGS
CREATE TABLE IF NOT EXISTS ai_agent_logs (
    id SERIAL PRIMARY KEY,
    agent_name TEXT,
    action TEXT,
    result TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
