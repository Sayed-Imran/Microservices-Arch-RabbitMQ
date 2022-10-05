import React, { useEffect } from 'react'
import {Link,useLocation} from "react-router-dom"
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
function CollapsibleExample() {

  let location = useLocation();
  useEffect(() => { }, [location]);

  const handleLogout = () => {
		localStorage.removeItem("token");
		window.location.reload();
	};

  return (
    <Navbar collapseOnSelect expand="lg" bg="primary" variant="dark">
      <Container>
        <Navbar.Brand to="/">Microservice-Based-Architecture</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto">
            <li className="nav-item">
              <Link className={`nav-link ${location.pathname === "/" ? "active" : ""}`} aria-current="page" to="/">Home</Link>
            </li>
            <li className="nav-item">
              <Link className={`nav-link ${location.pathname === "/product" ? "active" : ""}`} aria-current="page" to="/product">Product</Link>
            </li>
          </Nav>
          <Nav>
            <Link className="btn btn-outline-light m-2" to="/product/create">Add</Link>
            <Link className="btn btn-danger m-2" onClick={handleLogout}>Logout</Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default CollapsibleExample;