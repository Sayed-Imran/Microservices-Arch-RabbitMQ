import React from "react";
import {useState,useEffect} from "react"
import { useParams,useNavigate} from "react-router-dom"
  
function Update(){
  const navigate=useNavigate();

  const {id}=useParams();

  const [title,setTitle]=useState("")
  const [image,setImage]=useState("")


  useEffect(()=>{
    product()
    // eslint-disable-next-line
  },[])
  
  const product=()=>{
    var myHeaders = new Headers();
    myHeaders.append("Authorization", "Bearer "+localStorage.getItem("token"));

  var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
  };

  fetch(`${window.env.MICROSERVICE_2}/api/find_product/${id}`, requestOptions)
  .then(async(response)=>{
    var resp_json=await response.json()
    setImage(resp_json.image)
    setTitle(resp_json.title)
    //console.log(resp_json)

})
    .catch(error => console.log('error', error));
  }

    const handleSubmit=async(e)=>{
        e.preventDefault();
        var myHeaders = new Headers();
        myHeaders.append("Authorization", "Bearer "+localStorage.getItem("token"));
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
        "title": title,
        "image": image
        });

        var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
    };
    await fetch(`${window.env.MICROSERVICE_2}/api/update_product/${id}`, requestOptions)
        .then(response => response.text())
        //.then(result => console.log(result))
        .catch(error => console.log('error', error));
        navigate("/product")

    }       
    
    return(
        <div className="container">
      <div className="w-75 mx-auto shadow p-5">
        <h2 className="text-center mb-4">Edit</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <input
              type="text"
              className="form-control form-control-lg"
              placeholder="Title"
              name="title"
              value={title}
              onChange={(e)=>{setTitle(e.target.value)}}
            />
          </div>
          <div className="mb-3">
            <input
              type="text"
              className="form-control form-control-lg"
              placeholder="Image"
              name="image"
              value={image}
              onChange={(e)=>{setImage(e.target.value)}}
            />
          </div>
          <button  className="btn btn-warning w-100">Update</button>
        </form>
      </div>
    </div>
  
    )
}
export default Update;