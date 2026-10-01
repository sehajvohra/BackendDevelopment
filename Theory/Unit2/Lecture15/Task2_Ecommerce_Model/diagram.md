# E Commerce Conceptual Data Model

```mermaid
erDiagram
    CUSTOMER ||--|| CART : owns
    CUSTOMER ||--o{ ORDER : places
    CART }o--o{ PRODUCT : contains
    ORDER }o--o{ PRODUCT : includes

    CUSTOMER {
        int customer_id
        string name
        string email
    }

    CART {
        int cart_id
        int customer_id
    }

    PRODUCT {
        int product_id
        string name
        float price
    }

    ORDER {
        int order_id
        int customer_id
        date order_date
    }