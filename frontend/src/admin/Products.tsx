import React, {useEffect, useState} from 'react';
import Wrapper from "./Wrapper";
import {Product} from "../interface/product";
import {Link} from "react-router-dom";

const Products = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        (
            async () => {
                const response = await fetch(`${process.env.REACT_APP_MICROSERVICE_1}/api/find_products`);

                const data = await response.json();

                setProducts(data);
            }
        )();
    }, []);

    const del = async (product_id: string) => {
        if (window.confirm('Are you sure you want to delete this product?')) {
            await fetch(`${process.env.REACT_APP_MICROSERVICE_1}/api/delete_product/${product_id}`, {
                method: 'DELETE'
            });

            setProducts(products.filter((p: Product) => p.product_id !== product_id));
        }
    }

    return (
        <Wrapper>
            <div className="pt-3 pb-2 mb-3 border-bottom">
                <div className="btn-toolbar mb-2 mb-md-0">
                    <Link to='/admin/products/create' className="btn btn-sm btn-outline-secondary">Add</Link>
                </div>
            </div>

            <div className="table-responsive">
                <table className="table table-striped table-sm">
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Image</th>
                        <th>Title</th>
                        <th>Likes</th>
                        <th>Action</th>
                    </tr>
                    </thead>
                    <tbody>
                    {products.map(
                        (p: Product) => {
                            return (
                                <tr key={p.product_id}>
                                    <td>{p.product_id}</td>
                                    <td><img src={p.image} height="180"/></td>
                                    <td>{p.title}</td>
                                    <td>{p.likes}</td>
                                    <td>
                                        <div className="btn-group mr-2">
                                            <Link to={`/admin/products/${p.product_id}`}
                                                  className="btn btn-sm btn-outline-secondary">Edit</Link>
                                            <a href="#" className="btn btn-sm btn-outline-secondary"
                                               onClick={() => del(p.product_id)}
                                            >Delete</a>
                                        </div>
                                    </td>
                                </tr>
                            )
                        })}

                    </tbody>
                </table>
            </div>
        </Wrapper>
    );
};

export default Products;
