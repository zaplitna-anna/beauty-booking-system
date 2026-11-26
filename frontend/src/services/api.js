const API_BASE_URL = 'http://127.0.0.1:8000/api'

export async function getApiStatus() {
    const response = await fetch(`${API_BASE_URL}/users/status/`)

    if (!response.ok) {
        throw new Error('Не вдалося перевірити стан сервера')
    }

    return response.json()
}