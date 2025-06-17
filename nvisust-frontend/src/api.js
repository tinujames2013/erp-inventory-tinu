// src/api.js
import axios from 'axios'

export const api = axios.create({
  baseURL: '/api/'  // ✅ Don't use full URL, just /api/ (Django will handle it)
})
