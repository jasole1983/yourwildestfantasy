import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

export const fetchLeaguePosts = createAsyncThunk(
    "posts/getPosts", async (dispatch, getState) => {
        return await fetch("/api/posts/").then(
            (res) => res.json()
        );

    }
);

const postSlice = createSlice({
    name: "posts",
    initialState: {
        posts: [],
        status: null,
    },
    reducers: {
        addOneLeaguePost: (state, action) => (
            state.posts.push(action.payload)
        ),
        removeLeaguePost: (state, action) => (
            state.posts.filter((post) => post.id !== action.payload.id)
        ),
        getLeaguePosts: (state, action) => (
            state.posts = action.payload.map(post=> post) 
        ),
        clearState: (state) => (
            state = {}
        ),
    },
    extraReducers: {
        [fetchLeaguePosts.pending]: (state, action) => {
            state.status = "loading"
        },
        [fetchLeaguePosts.resolved]: (state, action) => {
            state.status = "success";
            state.posts = action.payload.map(post=> post)
        },
        [fetchLeaguePosts.rejected]: (state, action) => {
            state.status = "failed"
        }
    },
        
    // dispatch(fetchLeaguePosts())
})      




export const { addOneLeaguePost, removeLeaguePost, getLeaguePosts, clearState } = postSlice.actions

export const selectPosts = ({ posts }) => posts

export default postSlice.reducers


// export commentSlice.reducers as commentReducer
