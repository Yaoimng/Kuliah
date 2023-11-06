CREATE TABLE Products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE Suppliers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  contact_info VARCHAR(255)
);

CREATE TABLE Inventory (
  id SERIAL PRIMARY KEY,
  product_id INTEGER REFERENCES Products(id),
  category_id INTEGER REFERENCES Categories(id),
  supplier_id INTEGER REFERENCES Suppliers(id),
  quantity INTEGER,
  expiration_date DATE
);
