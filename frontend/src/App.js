import "./App.css"
import "../node_modules/bootstrap/dist/css/bootstrap.css";
import {Route,Routes,Navigate} from "react-router-dom"
import Signup from "./components/Auth/SignUp"
import Login from './components/Auth/Login';
import Home from './components/Home/Home';
import Product from './components/product/Product';
import Create from "./components/CRUD/Create"
import Update from './components/CRUD/Update';
import Navbar from './components/Home/Navbar';
function App() {
  const user = localStorage.getItem("token");
  return (
    <div>
      {user && <Navbar/>}
    <Routes >
      {user && <Route path="/" exact element={<Home />} />}
      <Route path="/" element={<Navigate replace to="/login" />} />

      {user && <Route path="/product" exact element={<Product />} />}
      <Route path="/product" element={<Navigate replace to="/login" />} />

      <Route path="/signup" element={<Signup/>}/>
      <Route path="/login" element={<Login/>}/>
      
      {user && <Route path="/product/create" exact element={<Create />} />}
      <Route path="/product/create" element={<Navigate replace to="/login" />} />

      {user && <Route path="/product/update/:id" exact element={<Update />} />}
      <Route path="/product/update/:id" element={<Navigate replace to="/login" />} />
      
    </Routes>
    </div>
    
  );
}

export default App;
