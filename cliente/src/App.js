import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./Login";
import Perfil from "./Perfil";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/perfil" element={<Perfil />} />
      </Routes>
    </Router>
  );
}

export default App;
