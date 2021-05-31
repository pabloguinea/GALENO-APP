import axios from 'axios';

const API_URL = 'http://localhost:8080/api/auth/';

class AuthService {
    login(user) {
        return axios
            .post('auth/jwt/create', {
                email: user.email,
                password: user.password
            })
            .then(response => {
                // save on localstorage (for static) or cookie (for server recommended)  
                if (response.data.accessToken) {
                    localStorage.setItem('user', JSON.stringify(response.data));
                }

                return response.data;
            });
    }

    logout() {
        // logout from server and clear cookie or localstorage
        localStorage.removeItem('user');
    }

    register(user) {
        return axios.post('v1/auth/users/', {
            first_name: user.username,
            email: user.email,
            password: user.password,
            re_password: user.re_password,
        });
    }
}

export default new AuthService();
