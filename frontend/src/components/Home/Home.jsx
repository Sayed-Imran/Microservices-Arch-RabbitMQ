import React, { useState, useEffect } from "react";
import LikeBtn from "../Like/LikeBtn";
import "./Home.css";
function Home() {

  const [products, setproduts] = useState([]);
  useEffect(() => {
    loadProducts();
  }, [products]);
  const loadProducts = async () => {
    var myHeaders = new Headers();
    myHeaders.append(
      "Authorization",
      "Bearer " + localStorage.getItem("token")
    );

    var requestOptions = {
      method: "GET",
      headers: myHeaders,
    };

    await fetch(`${window.env.MICROSERVICE_2}/api/find_products`, requestOptions)
      .then(async (response) => {
        const resp_json = await response.json();
        setproduts(resp_json);
      })
      .catch((error) => console.log("error", error));
  };

  return (
    <main role="main">
      <div className="album py-5 bg-light">
        <div className="container ">
          <div className="row">
            {products.map((product) => (
              <div className="col col-sm-4" key={product.product_id}>
                <div className="card mb-4 shadow-sm">
                  <img
                    className= "card-img-top "
                    src={product.image}
                    alt={product.image}
                  />
                  <div className="card-body">
                    <p className="card-text">{product.title}</p>
                    <div className="d-flex justify-content-between align-items-center">
                      <div className="btn-group">
                        <LikeBtn product={product} load={loadProducts} />
                      </div>
                      <small className="text-muted">{product.likes} likes</small>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </main>
  );
}
export default Home;
