CREATE TABLE hierarchy (
    id INT PRIMARY KEY,
    department TEXT,
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES hierarchy (id)
);

INSERT INTO hierarchy VALUES 
(1, 'CEO', NULL),
(2, 'VP Vendas', 1),
(3, 'VP Engenharia', 1),
(4, 'Gerente Backend', 3),
(5, 'Dev Junior', 4);

WITH RECURSIVE SubordinateTree AS (
    SELECT 
        id, 
        department, 
        parent_id,
        0 as level
    FROM 
        hierarchy
    WHERE 
        id = 1
    UNION ALL
    SELECT 
        h.id, 
        h.department, 
        h.parent_id,
        st.level + 1
    FROM 
        hierarchy h
    INNER JOIN 
        SubordinateTree st ON h.parent_id = st.id
)
SELECT * FROM SubordinateTree;