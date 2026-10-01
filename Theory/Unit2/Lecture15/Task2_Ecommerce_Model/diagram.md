# E Commerce Conceptual Data Model

```mermaid
flowchart LR

    CUSTOMER["CUSTOMER<br/>customer_id<br/>name<br/>email"]

    CART["CART<br/>cart_id<br/>customer_id"]

    PRODUCT["PRODUCT<br/>product_id<br/>name<br/>price"]

    ORDER["ORDER<br/>order_id<br/>customer_id<br/>order_date"]

    CUSTOMER -->|"owns"| CART
    CUSTOMER -->|"places"| ORDER
    CART -->|"contains"| PRODUCT
    ORDER -->|"includes"| PRODUCT