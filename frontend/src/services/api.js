const API_URL = '/api/reservas';

export async function fetchReservations() {
  const response = await fetch(API_URL);
  if (!response.ok) throw new Error('Error al obtener reservas');
  return await response.json();
}

export async function createReservation(data) {
  const response = await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!response.ok) throw new Error('Error al crear reserva');
  return await response.json();
}

export async function updateReservation(id, data) {
  const response = await fetch(`${API_URL}/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!response.ok) throw new Error('Error al actualizar reserva');
  return await response.json();
}