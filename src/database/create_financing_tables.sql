-- USERS
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    role TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- BUYERS
CREATE TABLE buyers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    credit_score INTEGER,
    income INTEGER,
    city TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- INVESTORS
CREATE TABLE investors (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    preferred_city TEXT,
    max_budget INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- VEHICLES
CREATE TABLE vehicles (
    id SERIAL PRIMARY KEY,
    make TEXT,
    model TEXT,
    year INTEGER,
    price INTEGER,
    mileage INTEGER,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- VEHICLE LEADS
CREATE TABLE vehicle_leads (
    id SERIAL PRIMARY KEY,
    vehicle_id INTEGER,
    buyer_id INTEGER,
    lead_score INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- FINANCING APPLICATIONS
CREATE TABLE financing_applications (
    id SERIAL PRIMARY KEY,
    buyer_id INTEGER,
    vehicle_id INTEGER,
    loan_amount INTEGER,
    down_payment INTEGER,
    interest_rate FLOAT,
    term_months INTEGER,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- LOAN DECISIONS
CREATE TABLE loan_decisions (
    id SERIAL PRIMARY KEY,
    application_id INTEGER,
    decision TEXT,
    approved_amount INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- PROPERTIES
CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    address TEXT,
    city TEXT,
    state TEXT,
    price INTEGER,
    arv INTEGER,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- PROPERTY LEADS
CREATE TABLE property_leads (
    id SERIAL PRIMARY KEY,
    property_id INTEGER,
    score INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- WHOLESALE DEALS
CREATE TABLE wholesale_deals (
    id SERIAL PRIMARY KEY,
    property_id INTEGER,
    investor_id INTEGER,
    contract_price INTEGER,
    assignment_fee INTEGER,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- PROPERTY COMPS
CREATE TABLE property_comps (
    id SERIAL PRIMARY KEY,
    property_id INTEGER,
    comp_price INTEGER,
    comp_address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DEAL ANALYSIS
CREATE TABLE deal_analysis (
    id SERIAL PRIMARY KEY,
    property_id INTEGER,
    arv INTEGER,
    repair_cost INTEGER,
    profit INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- AI AGENTS
CREATE TABLE ai_agents (
    id SERIAL PRIMARY KEY,
    agent_name TEXT,
    agent_type TEXT,
    status TEXT,
    last_run TIMESTAMP
);

-- AGENT TASKS
CREATE TABLE agent_tasks (
    id SERIAL PRIMARY KEY,
    agent_id INTEGER,
    task_name TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- AGENT LOGS
CREATE TABLE agent_logs (
    id SERIAL PRIMARY KEY,
    agent_id INTEGER,
    action TEXT,
    result TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DATA SOURCES
CREATE TABLE data_sources (
    id SERIAL PRIMARY KEY,
    name TEXT,
    type TEXT,
    url TEXT
);

-- SCRAPER RUNS
CREATE TABLE scraper_runs (
    id SERIAL PRIMARY KEY,
    source_id INTEGER,
    records_found INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ALERTS
CREATE TABLE alerts (
    id SERIAL PRIMARY KEY,
    alert_type TEXT,
    message TEXT,
    sent BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- NOTIFICATIONS
CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    message TEXT,
    read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DEAL PIPELINE
CREATE TABLE deal_pipeline (
    id SERIAL PRIMARY KEY,
    deal_type TEXT,
    reference_id INTEGER,
    stage TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- AI DECISIONS
CREATE TABLE ai_decisions (
    id SERIAL PRIMARY KEY,
    agent_id INTEGER,
    decision TEXT,
    confidence FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- MARKET DATA
CREATE TABLE market_data (
    id SERIAL PRIMARY KEY,
    city TEXT,
    avg_price INTEGER,
    avg_rent INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- API KEYS
CREATE TABLE api_keys (
    id SERIAL PRIMARY KEY,
    service TEXT,
    api_key TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- SYSTEM CONFIG
CREATE TABLE system_config (
    id SERIAL PRIMARY KEY,
    config_key TEXT,
    config_value TEXT
);

-- PLATFORM METRICS
CREATE TABLE platform_metrics (
    id SERIAL PRIMARY KEY,
    metric_name TEXT,
    metric_value INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
