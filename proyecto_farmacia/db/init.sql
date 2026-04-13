CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS puntos_interes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    categoria VARCHAR(50),
    geom GEOMETRY(Point, 4326)
);

-- Carga inicial de 5 puntos (Requisito UMG)
INSERT INTO puntos_interes (nombre, descripcion, categoria, geom) VALUES
('Farmacia Galeno', 'Servicio 24 horas', 'Salud', ST_GeomFromText('POINT(-90.531 14.481)', 4326)),
('Farmacia Cruz Verde', 'Ubicada en el centro', 'Salud', ST_GeomFromText('POINT(-90.535 14.485)', 4326)),
('Parque Central', 'Punto de reunión Villa Canales', 'Cultural', ST_GeomFromText('POINT(-90.527 14.482)', 4326)),
('Estación Shell', 'Combustible y tienda', 'Servicio', ST_GeomFromText('POINT(-90.538 14.488)', 4326)),
('Restaurante Local', 'Comida típica', 'Gastronómico', ST_GeomFromText('POINT(-90.533 14.483)', 4326));
