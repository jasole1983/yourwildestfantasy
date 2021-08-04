import { createSlice } from "@reduxjs/toolkit";


export const postSlices = createSlice({
    name: "post",
    initialState,
    reducers:{
        addOne: (state, action) => state.push(action.payload),
        remove: (state, action) => state.remove(action.payload),
        getAll: (state, action) => state.concat(action.payload),
        clear: (state, action)  => state = {},
        }
})      

export const { addOne, remove, getAll, clear } = postSlices.actions

export default postSlices.reducer