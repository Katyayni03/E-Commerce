function ProductDetail({ product, onBack }) {
    return (
      <div className="product-detail">
        <button onClick={onBack}>← Back</button>
        <img src={product.image} alt={product.name} />
        <h2>{product.name}</h2>
        <p><strong>₹{product.price}</strong></p>
        <p>{product.description}</p>
        <input type="number" min="1" defaultValue={1} />
        <button>Add to Cart</button>
        <button>Buy Now</button>
      </div>
    );
  }
  
