import { configureStore } from '@reduxjs/toolkit';
import rootReducers from './indexR';

const store = configureStore({
    reducer: rootReducers,
});

export default store