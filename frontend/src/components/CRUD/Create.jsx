import React from "react";
import {useState} from "react"
import { useNavigate } from "react-router-dom";
function Create(){
  const navigate=useNavigate();


    const [data,setData]=useState({
        title:"",
        image:""
    });
    const handleChange=({currentTarget: input})=>{
        setData({...data,[input.name]:input.value})

    };
    const handleSubmit=async(e)=>{
        e.preventDefault();
        var myHeaders = new Headers();
        myHeaders.append("Authorization", "Bearer "+localStorage.getItem("token"));
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
            "title": data.title,
            "image": data.image
        });

        var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw
        };

    fetch(`${window.env.MICROSERVICE_2}/api/create_product`, requestOptions)
        .then(response => response.json())
        //.then(result => console.log(result))
        .catch(error => console.log('error', error));
        navigate("/")
    } 
    return(
        <div className="container">
        <div className="w-75 mx-auto shadow p-5">
          <h2 className="text-center mb-4">Add A Product</h2>

          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <input type="text" 
              className="form-control form-control-lg" 
              placeholder="Title" 
              name="title" 
              value={data.title} onChange={handleChange} />
            </div>
            <div className="mb-3">
              <input
                type="text"
                className="form-control form-control-lg"
                placeholder="Image"
                name="image"
                value={data.image}
                onChange={handleChange}
              />
            </div>
            <button className="btn btn-primary w-100">Add User</button>
          </form>
        </div>
      </div>
  
    )
}
export default Create;