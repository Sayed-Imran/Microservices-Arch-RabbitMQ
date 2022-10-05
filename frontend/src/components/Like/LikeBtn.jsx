import React from "react";
import {AiTwotoneHeart} from "react-icons/ai"
function LikeBtn(props) {


  const like = async (id) => {
    var myHeaders = new Headers();
    myHeaders.append(
      "Authorization",
      "Bearer " + localStorage.getItem("token")
    );
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
      product_id: id,
    });

    var requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
    };

    await fetch(`${process.env.REACT_APP_MICROSERVICE_3}/api/like/${id}`, requestOptions)
      .then((response) => response.json())
      //.then((result) => console.log(result))
      .catch((error) => console.log("error", error));
      
  };
  return (
    <>
      <button type="button"
        className="btn btn-sm btn-outline-secondary"
        onClick={() => like(props.product.product_id)} >
          <AiTwotoneHeart/>
      </button>
    </>
  );
}

export default LikeBtn;
