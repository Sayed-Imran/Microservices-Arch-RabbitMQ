import React from "react";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Pic from "../assests/pic1.png"
import "./Signup.css"

function Signup(){
    const [data,setData]=useState({
        fullName:"",
        username:"",
        password:""
    });

    const navigate =useNavigate();
    
    const handleChange=({currentTarget: input})=>{
        setData({...data,[input.name]:input.value})

    };
    const handleSubmit = async (e) => {
		e.preventDefault();
		var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
        "name": data.fullName,
        "email": data.username,
        "password": data.password
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
  
    };

    await fetch(`${process.env.REACT_APP_MICROSERVICE_1}/api/signup`, requestOptions)
    .then(navigate("/signin")) 
    //.then(result => console.log(result))
     //   .catch(error => console.log('error', error));
    }
    return(
        <section className="vh-100">
            <div className="container-fluid h-custom">
                <div className="row d-flex justify-content-center align-items-center h-100">
                    <div className="col-md-9 col-lg-6 col-xl-5">
                        <img className="img-fluid" src={Pic} alt="micro-service"  />
                    </div>
                    <div className="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
                        <form onSubmit={handleSubmit}>  
                            <div className="form-outline mb-4">
                                <input type="email" id="form3Example3" className="form-control form-control-lg"
                                placeholder="Full Name" name="fullName" value={data.fullName} onChange={handleChange} required/>
                            </div>    
                            <div className="form-outline mb-4">
                                <input type="email" id="form3Example3" className="form-control form-control-lg"
                                placeholder="Email" name="username" value={data.username} onChange={handleChange} required/>
                            </div>
      
                            <div className="form-outline mb-3">
                                <input type="password" id="form3Example4" className="form-control form-control-lg"
                                placeholder="Password" name="password" value={data.password} onChange={handleChange} required/>
                            </div>
      
                            <div className="text-center text-lg-start mt-4 pt-2">
                                <button  className="btn btn-primary btn-lg"
                                style={{paddingLeft:" 2.5rem" , paddingRight: "2.5rem"}}>Signup</button>
                                <p className="small fw-bold mt-2 pt-1 mb-0">Don't have an account? <Link to="/login"
                                className="link-danger">Login</Link></p>
                            </div>
      
                        </form>
                    </div>
                </div>
            </div>
      </section>
                
)
}
export default Signup;