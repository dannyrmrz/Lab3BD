import React, { useState, useEffect } from 'react';
import { createReservation, updateReservation } from '../services/api';

const ReservationForm = ({ reservation, onSave }) => {
  const [formData, setFormData] = useState({
    id_usuario: reservation ? reservation.id_usuario : '',
    id_cola: reservation ? reservation.id_cola : '',
    estado: reservation ? reservation.estado : 'pendiente',
    hora_reserva: reservation ? reservation.hora_reserva : '',
  });

  useEffect(() => {
    if (reservation) {
      setFormData({
        id_usuario: reservation.id_usuario,
        id_cola: reservation.id_cola,
        estado: reservation.estado,
        hora_reserva: reservation.hora_reserva,
      });
    }
  }, [reservation]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (reservation) {
      await updateReservation(reservation.id_reserva, formData);
    } else {
      await createReservation(formData);
    }
    onSave();
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="id_usuario">Usuario ID:</label>
        <input
          type="number"
          name="id_usuario"
          value={formData.id_usuario}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="id_cola">Cola ID:</label>
        <input
          type="number"
          name="id_cola"
          value={formData.id_cola}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="estado">Estado:</label>
        <select
          name="estado"
          value={formData.estado}
          onChange={handleChange}
        >
          <option value="pendiente">Pendiente</option>
          <option value="confirmada">Confirmada</option>
          <option value="cancelada">Cancelada</option>
        </select>
      </div>
      <div>
        <label htmlFor="hora_reserva">Hora de Reserva:</label>
        <input
          type="time"
          name="hora_reserva"
          value={formData.hora_reserva}
          onChange={handleChange}
          required
        />
      </div>
      <button type="submit">{reservation ? 'Actualizar' : 'Crear'} Reserva</button>
    </form>
  );
};

export default ReservationForm;