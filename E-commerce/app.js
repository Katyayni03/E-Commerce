import React, { useState } from 'react';
import Header from './components/Header';
import Filters from './components/Filters';
import ProductList from './components/ProductList';
import ProductDetail from './components/ProductDetail';
import products from './data/products';

function App() {
  const [selectedProduct, setSelectedProduct] = useState(null);

  return (
    <div>
      <Header />
      {selectedProduct ? (
        <ProductDetail product={selectedProduct} onBack={() => setSelectedProduct(null)} />
      ) : (
        <>
          <Filters />
          <ProductList products={products} onSelect={setSelectedProduct} />
        </>
      )}
    </div>
  );
}

export default App;
