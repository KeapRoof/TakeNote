export interface User {
    id: number;
    username: string;
    email: string;
}

export interface LoginResponse {
    message: string;
    user: User;
}

export interface LoginGet {
    email: string;
    password: string;
}

export interface CreateResponse {
    message: string;
    user: User;
}
