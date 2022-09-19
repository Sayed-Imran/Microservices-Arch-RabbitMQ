import React, {useEffect, useState} from 'react';
import {Product} from "../interface/product";

const Main = () => {
    const [products, setProducts] = useState([] as Product[]);

    useEffect(() => {
        (
            async () => {
                const response = await fetch(`${process.env.REACT_APP_MICROSERVICE_1}/api/find_products`);

                const data = await response.json();

                setProducts(data);
            }
        )();
    }, []);

    const like = async (product_id: string) => {
        await fetch(`${process.env.REACT_APP_MICROSERVICE_2}/api/like/${product_id}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}
        });

        setProducts(products.map(
            (p: Product) => {
                if (p.product_id === product_id) {
                    p.likes++;
                }

                return p;
            }
        ));
    }

    return (
        <main role="main">
            <div className="album py-5 bg-light">
                <div className="container">
                    <div className="row">
                        {products.map(
                            (p: Product) => {
                                return (
                                    <div className="col-md-4" key={p.product_id}>
                                        <div className="card mb-4 shadow-sm">
                                            <img src={p.image} height="180" alt={p.image}/>
                                            <div className="card-body">
                                                <p className="card-text">{p.title}</p>
                                                <div className="d-flex justify-content-between align-items-center">
                                                    <div className="btn-group">
                                                        <button type="button"
                                                                className="btn btn-sm btn-outline-secondary"
                                                                onClick={() => like(p.product_id)}
                                                        >
                                                            Like
                                                        </button>
                                                    </div>
                                                    <small className="text-muted">{p.likes} likes</small>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                )
                            }
                        )}
                    </div>
                </div>
            </div>

        </main>
    );
};

export default Main;
