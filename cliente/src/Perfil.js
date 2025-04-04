// import React, { useEffect, useState } from "react";

// const Perfil = () => {
//   const [usuarios, setUsuarios] = useState([]);
//   const [usuarioLogado, setUsuarioLogado] = useState(null);
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState(null);
//   const [saldo, setSaldo] = useState({});
//   const usuarioLocal = JSON.parse(localStorage.getItem("user"));

//   const ID_LOGADO = usuarioLocal.id; // ID do usuário logado (fixo por enquanto)

//   // Buscar usuário logado
//   const fetchUsuarioLogado = async () => {
//     try {
//       const response = await fetch(
//         `http://127.0.0.1:8000/api/usuarios/${ID_LOGADO}/`
//       );

//       if (!response.ok) throw new Error("Erro ao buscar usuário logado.");

//       const data = await response.json();
//       setUsuarioLogado(data);
//     } catch (err) {
//       console.error("Erro ao buscar usuário logado:", err);
//     }
//   };

//   // Buscar todos os usuários
//   const fetchUsuarios = async () => {
//     try {
//       const response = await fetch("http://127.0.0.1:8000/api/usuarios/", {
//         method: "GET",
//         headers: {
//           "Content-Type": "application/json",
//         },
//       });

//       if (!response.ok) {
//         throw new Error(`Erro ao buscar usuários: ${response.status}`);
//       }

//       const data = await response.json();
//       setUsuarios(Array.isArray(data) ? data : []);
//     } catch (err) {
//       console.error("Erro:", err);
//       setError(err.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   // Transferir saldo
//   const atualizarSaldo = async (destinatarioId) => {
//     const valor = saldo[destinatarioId] || 0;

//     try {
//       const response = await fetch("http://127.0.0.1:8000/api/transferir/", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify({
//           remetente_id: ID_LOGADO,
//           destinatario_id: destinatarioId,
//           valor: parseFloat(valor),
//         }),
//       });

//       if (!response.ok) throw new Error("Erro ao transferir saldo.");

//       alert("Transferência realizada com sucesso!");
//       window.location.reload();
//       fetchUsuarios();
//       fetchUsuarioLogado(); // Atualiza saldo do topo também
//     } catch (err) {
//       console.error("Erro:", err);
//       alert("Erro ao transferir saldo.");
//     }
//   };

//   useEffect(() => {
//     fetchUsuarioLogado();
//     fetchUsuarios();
//   }, []);

//   return (
//     <div style={{ padding: "20px" }}>
//       <h1>Perfil</h1>

//       <div style={{ padding: "20px" }}>
//         {usuarioLocal && (
//           <h1>
//             ID: {usuarioLocal.id} | Nome: {usuarioLocal.nome} | Email:{" "}
//             {usuarioLocal.email} | Saldo: R${" "}
//             {parseFloat(usuarioLocal.saldo).toFixed(2)}
//           </h1>
//         )}
//         {/* ... restante do código */}
//       </div>

//       {loading && <p>Carregando...</p>}
//       {error && <p style={{ color: "red" }}>{error}</p>}

//       <ul>
//         {usuarios
//           .filter((usuario) => usuario.id !== usuarioLocal?.id) // <- filtra o logado
//           .map((usuario) => (
//             <li key={usuario.id} style={{ marginBottom: "20px" }}>
//               <p>
//                 {usuario.nome} - {usuario.email} - Saldo: R${" "}
//                 {parseFloat(usuario.saldo).toFixed(2)}
//               </p>

//               <input
//                 type="number"
//                 placeholder="Valor a transferir"
//                 value={saldo[usuario.id] || ""}
//                 onChange={(e) =>
//                   setSaldo({ ...saldo, [usuario.id]: e.target.value })
//                 }
//               />
//               <button onClick={() => atualizarSaldo(usuario.id)}>
//                 Transferir Saldo
//               </button>
//             </li>
//           ))}
//       </ul>
//     </div>
//   );
// };

// export default Perfil;

import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import "bootstrap/dist/css/bootstrap.min.css";

const Perfil = () => {
  const [usuarios, setUsuarios] = useState([]);
  const [usuarioLogado, setUsuarioLogado] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [saldo, setSaldo] = useState({});
  const [usuarioLocal, setUsuarioLocal] = useState(null);
  useEffect(() => {
    const userFromStorage = JSON.parse(localStorage.getItem("user"));
    setUsuarioLocal(userFromStorage);
  }, []);

  const navigate = useNavigate();

  const ID_LOGADO = usuarioLocal?.id;

  const fetchUsuarioLogado = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/usuarios/${ID_LOGADO}/`
      );
      if (!response.ok) throw new Error("Erro ao buscar usuário logado.");
      const data = await response.json();
      setUsuarioLogado(data);

      // Atualiza o localStorage e o estado local
      localStorage.setItem("user", JSON.stringify(data));
      setUsuarioLocal(data); // 🔥 isso aqui é essencial para refletir no render
    } catch (err) {
      console.error("Erro ao buscar usuário logado:", err);
    }
  };

  const fetchUsuarios = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/usuarios/");
      if (!response.ok) throw new Error("Erro ao buscar usuários.");
      const data = await response.json();
      setUsuarios(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error("Erro:", err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const atualizarSaldo = async (destinatarioId) => {
    const valor = saldo[destinatarioId] || 0;
    try {
      const response = await fetch("http://127.0.0.1:8000/api/transferir/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          remetente_id: ID_LOGADO,
          destinatario_id: destinatarioId,
          valor: parseFloat(valor),
        }),
      });
      if (!response.ok) throw new Error("Erro ao transferir saldo.");

      alert("Transferência realizada com sucesso!");
      navigate("/");
    } catch (err) {
      console.error("Erro:", err);
      alert("Erro ao transferir saldo.");
    }
  };

  useEffect(() => {
    fetchUsuarioLogado();
    fetchUsuarios();
  }, []);

  return (
    <div className="container mt-4">
      {usuarioLocal && (
        <div className="card p-3 mb-4">
          <p>
            <strong>Nome:</strong> {usuarioLocal.nome}
          </p>
          <p>
            <strong>Saldo:</strong> R${" "}
            {parseFloat(usuarioLocal.saldo).toFixed(2)}
          </p>
        </div>
      )}

      {loading && <p>Carregando...</p>}
      {error && <p className="text-danger">{error}</p>}

      <ul className="list-group">
        {usuarios
          .filter((usuario) => usuario.id !== usuarioLocal?.id)
          .map((usuario) => (
            <li
              key={usuario.id}
              className="list-group-item d-flex justify-content-between align-items-center"
            >
              <div>
                <p className="mb-1">
                  <strong>{usuario.nome}</strong>
                </p>
              </div>
              <div className="input-group" style={{ maxWidth: "300px" }}>
                <input
                  type="number"
                  className="form-control"
                  placeholder="Valor a transferir"
                  value={saldo[usuario.id] || ""}
                  onChange={(e) =>
                    setSaldo({ ...saldo, [usuario.id]: e.target.value })
                  }
                />
                <button
                  className="btn btn-primary"
                  onClick={() => atualizarSaldo(usuario.id)}
                >
                  Transferir
                </button>
              </div>
            </li>
          ))}
      </ul>
    </div>
  );
};

export default Perfil;
