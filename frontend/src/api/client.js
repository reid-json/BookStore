const API_BASE = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8000';

function getToken() {
  return localStorage.getItem('jwt_access') || '';
}

export async function apiFetch(path, { method = 'GET', body, headers = {}, auth = true } = {}) {
  const h = { 'Content-Type': 'application/json', ...headers };
  if (auth && getToken()) h['Authorization'] = `Bearer ${getToken()}`;
  const res = await fetch(`${API_BASE}${path}`, {
    method,
    headers: h,
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
  return res.json();
}

export async function login(username, password) {
  const data = await apiFetch('/api/auth/login/', { method: 'POST', auth: false, body: { username, password } });
  localStorage.setItem('jwt_access', data.access);
  localStorage.setItem('jwt_refresh', data.refresh);
  return data;
}

export async function refresh() {
  const refresh = localStorage.getItem('jwt_refresh');
  if (!refresh) throw new Error('No refresh token');
  const data = await apiFetch('/api/auth/refresh/', { method: 'POST', auth: false, body: { refresh } });
  localStorage.setItem('jwt_access', data.access);
  return data;
}

export function logout() {
  localStorage.removeItem('jwt_access');
  localStorage.removeItem('jwt_refresh');
}

export async function registerUser({ username, email, password }) {
  return apiFetch('/api/auth/register/', { method: 'POST', auth: false, body: { username, email, password } });
}

export async function me() {
  try {
    return await apiFetch('/api/auth/me/');
  } catch (e) {
    // try one refresh
    await refresh();
    return apiFetch('/api/auth/me/');
  }
}