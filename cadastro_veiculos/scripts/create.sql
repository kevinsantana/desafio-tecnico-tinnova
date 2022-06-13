-- -----------------------------------------------------
-- DROP TABLES
-- -----------------------------------------------------
DROP TABLE IF EXISTS public.VEICULOS CASCADE;
-- -----------------------------------------------------
-- Table public.REVENDEDOR
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.VEICULOS (
  ID_VEICULOS SERIAL PRIMARY KEY,
  VEICULO VARCHAR(160) NOT NULL,
  MARCA VARCHAR(100) NOT NULL,
  ANO INTEGER NOT NULL,
  DESCRICAO VARCHAR(300) NOT NULL,
  VENDIDO BOOLEAN NOT NULL,
  CREATED TIMESTAMP NOT NULL,
  UPDATED TIMESTAMP
);
