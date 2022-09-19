import React, {PropsWithRef, SyntheticEvent, useEffect, useState} from 'react';
import Wrapper from "./Wrapper";
import {useNavigate } from 'react-router-dom';
import {Product} from "../interface/product";

const ProductsEdit = (props: PropsWithRef<any>) => {
    const [title, setTitle] = useState('');
    const [image, setImage] = useState('');
    const [redirect, setRedirect] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        (
            async () => {
                const response = await fetch(`${process.env.REACT_APP_MICROSERVICE_1}/api/find_product/${props.match.params.id}`);

                const product: Product = await response.json();

                setTitle(product.title);
                setImage(product.image)
            }
        )();
    }, []);

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        await fetch(`${process.env.REACT_APP_MICROSERVICE_1}/api/update_product/${props.match.params.id}`, {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                title,
                image
            })
        });

        setRedirect(true);
    }

    if (redirect) {
        navigate('/admin/products')
    }

    return (
        <Wrapper>
            <form onSubmit={submit}>
                <div className="form-group">
                    <label>Title</label>
                    <input type="text" className="form-control" name="title"
                           defaultValue={title}
                           onChange={e => setTitle(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Image</label>
                    <input type="text" className="form-control" name="image"
                           defaultValue={image}
                           onChange={e => setImage(e.target.value)}
                    />
                </div>
                <button className="btn btn-outline-secondary">Save</button>
            </form>
        </Wrapper>
    );
};

export default ProductsEdit;
