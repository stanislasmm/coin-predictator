drop database if exists coin_predictator;
create database coin_predictator owner postgres;
\connect coin_predictator

CREATE TABLE prices
(
  id bigserial PRIMARY KEY, -- The primary key
  time DATE NOT NULL,
  close NUMERIC(12,4) NOT NULL,
  high NUMERIC(12,4) NOT NULL,
  low NUMERIC(12,4) NOT NULL,
  open NUMERIC(12,4) NOT NULL,
  volumefrom INTEGER NOT NULL,
  volumeto INTEGER NOT NULL,
  pairfrom VARCHAR (5) NOT NULL,
  pairto VARCHAR (5) NOT NULL
)