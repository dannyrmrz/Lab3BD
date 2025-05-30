import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import ReservationList from './components/ReservationList';
import ReservationForm from './components/ReservationForm';
import {
  fetchReservations,
  createReservation,
  updateReservation,
} from "./services/api";

function App() {
  const [reservations, setReservations] = useState([]);
  const [error, setError] = useState("");
  const [form, setForm] = useState({
    id_usuario: "",
    id_cola: "",
    estado: "pendiente",
    hora_reserva: "",
  });

  useEffect(() => {
    loadReservations();
  }, []);

  async function loadReservations() {
    try {
      const data = await fetchReservations();
      setReservations(data);
      setError("");
    } catch (err) {
      setError("Error fetching reservations: " + err.message);
    }
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      await createReservation(form);
      setForm({
        id_usuario: "",
        id_cola: "",
        estado: "pendiente",
        hora_reserva: "",
      });
      loadReservations();
    } catch (err) {
      setError("Error creating reservation: " + err.message);
    }
  }

  return (
    <Router>
      <Navbar />
      <div style={styles.container}>
        <h1 style={styles.title}>Theme Park Reservations</h1>
        <div style={styles.flex}>
          <div style={styles.formContainer}>
            <h2>Crear Reserva</h2>
            <form onSubmit={handleSubmit} style={styles.form}>
              <input
                style={styles.input}
                type="number"
                placeholder="ID Usuario"
                value={form.id_usuario}
                onChange={(e) =>
                  setForm({ ...form, id_usuario: e.target.value })
                }
                required
              />
              <input
                style={styles.input}
                type="number"
                placeholder="ID Cola"
                value={form.id_cola}
                onChange={(e) => setForm({ ...form, id_cola: e.target.value })}
                required
              />
              <select
                style={styles.input}
                value={form.estado}
                onChange={(e) => setForm({ ...form, estado: e.target.value })}
              >
                <option value="pendiente">Pendiente</option>
                <option value="confirmada">Confirmada</option>
                <option value="cancelada">Cancelada</option>
              </select>
              <input
                style={styles.input}
                type="time"
                placeholder="Hora Reserva"
                value={form.hora_reserva}
                onChange={(e) =>
                  setForm({ ...form, hora_reserva: e.target.value })
                }
                required
              />
              <button style={styles.button} type="submit">
                Crear
              </button>
            </form>
          </div>
          <div style={styles.listContainer}>
            <h2>Reservas</h2>
            {error && <div style={styles.error}>{error}</div>}
            <table style={styles.table}>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Usuario</th>
                  <th>Cola</th>
                  <th>Estado</th>
                  <th>Hora</th>
                </tr>
              </thead>
              <tbody>
                {reservations.map((r) => (
                  <tr key={r.id}>
                    <td>{r.id}</td>
                    <td>{r.id_usuario}</td>
                    <td>{r.id_cola}</td>
                    <td>{r.estado}</td>
                    <td>{r.hora_reserva}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <Routes>
        <Route path="/" element={<ReservationList />} />
        <Route path="/reservations/new" element={<ReservationForm />} />
        <Route path="/reservations/edit/:id" element={<ReservationForm />} />
      </Routes>
    </Router>
  );
}

const styles = {
  container: { fontFamily: "Arial", padding: 40, background: "#f8f8ff", minHeight: "100vh" },
  title: { color: "#2d2d2d", marginBottom: 20 },
  flex: { display: "flex", gap: 40 },
  formContainer: { background: "#fff", padding: 20, borderRadius: 8, boxShadow: "0 2px 8px #ddd" },
  form: { display: "flex", flexDirection: "column", gap: 10 },
  input: { padding: 8, borderRadius: 4, border: "1px solid #ccc" },
  button: { padding: 10, background: "#007bff", color: "#fff", border: "none", borderRadius: 4, cursor: "pointer" },
  listContainer: { flex: 1, background: "#fff", padding: 20, borderRadius: 8, boxShadow: "0 2px 8px #ddd" },
  table: { width: "100%", borderCollapse: "collapse" },
  error: { color: "red", marginBottom: 10 },
};

export default App;