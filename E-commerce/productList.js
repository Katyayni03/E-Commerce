import ProductCard from './ProductCard';

function ProductList({ products, onSelect }) {
  return (
    <div className="grid">
      {products.map(p => (
        <ProductCard key={p.id} product={p} onSelect={onSelect} />
      ))}
    </div>
  );
}
