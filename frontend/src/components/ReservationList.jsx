import React, { useEffect, useState } from 'react';
import { fetchReservations } from '../services/api';

const ReservationList = () => {
  const [reservations, setReservations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getReservations = async () => {
      try {
        const data = await fetchReservations();
        setReservations(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    getReservations();
  }, []);

  if (loading) {
    return <div>Loading reservations...</div>;
  }

  if (error) {
    return <div>Error fetching reservations: {error}</div>;
  }

  return (
    <div>
      <h2>Reservation List</h2>
      <ul>
        {reservations.map((reservation) => (
          <li key={reservation.id_reserva}>
            User ID: {reservation.id_usuario}, Cola ID: {reservation.id_cola}, Status: {reservation.estado}, Time: {reservation.hora_reserva}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ReservationList;