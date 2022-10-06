import React from "react";
import { useState } from "react";
import { Link } from "react-router-dom";
import "./Login.css"
import Pic from "../assests/pic1.png"
function Signin(){
    const [data,setData]=useState({
        username:"",
        password:""
    });
    const handleChange=({currentTarget: input})=>{
        setData({...data,[input.name]:input.value})

    };
    const handleSubmit=async(e)=>{
        e.preventDefault();
        const formdata = new FormData();
        formdata.append("username",data.username);
        formdata.append("password",data.password);
        
        const requestOptions = {
          method: 'POST',
          body: formdata,
        };
        
        await fetch(`${window.env.MICROSERVICE_1}/api/login`, requestOptions)
            .then(async(response)=>{
                var resp_json=await response.json()
                console.log(resp_json.detail.access_token)
                localStorage.setItem("token",resp_json.detail.access_token)
                window.location = "/";

            })
            .catch(error => console.log('error', error));
    };
    return(
        <section className="vh-100">
            <div className="container-fluid h-custom">
                <div className="row d-flex justify-content-center align-items-center h-100">
                    <div className="col-md-9 col-lg-6 col-xl-5">
                        <img className="img-fluid" src={Pic} alt=""  />
                    </div>
                    <div className="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
                        <form onSubmit={handleSubmit}>      
                            <div className="form-outline mb-4">
                                <input type="email" id="form3Example3" className="form-control form-control-lg"
                                placeholder="Email" name="username" value={data.username} onChange={handleChange} />
                             </div>
      
                            <div className="form-outline mb-3">
                                <input type="password" id="form3Example4" className="form-control form-control-lg"
                                placeholder="password" name="password" value={data.password} onChange={handleChange} />
                            </div>
      
                            <div className="text-center text-lg-start mt-4 pt-2">
                                <button  className="btn btn-primary btn-lg"
                                    style={{paddingLeft:" 2.5rem" , paddingRight: "2.5rem"}}>
                                    Login
                                </button>
                                <p className="small fw-bold mt-2 pt-1 mb-0">Don't have an account? <Link to="/signup"
                                 className="link-danger">Register</Link></p>
                            </div>
      
                        </form>
                    </div>
                </div>
            </div>
        </section>
                    
    )
}
export default Signin;