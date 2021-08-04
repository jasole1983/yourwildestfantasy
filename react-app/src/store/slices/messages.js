import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

export const fetchLeaguePosts = createAsyncThunk(
    "posts/getLeaguePosts", async () => {
        const res = await fetch("/api/posts/:leagueId")
        const data = await res.json()

    }
)

const initialState = {
        posts: [],
    };




export const postSlice = createSlice({
    name: "posts",
    initialState: {
        list: [],
        status: null,
    }
    reducers:{
        addOne(state, action) {
            state.push(action.payload)
        },
        remove(state, action) {
            state.remove(action.payload)
        },
        getAll(state, action) {
            {...state, } 
        },
        clear(state, action) {
            state = {}
        },
        }
})      

export const { addOne, remove, getAll, clear } = postSlice.actions

export default postSlice.reducer