import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { useDispatch } from "react-redux";

export const getPosts = createAsyncThunk("posts/getPosts", async () => {
    return await fetch(`/api/posts/`, 'GET').then((res) => res.json())});
    
    
    export const removePost = createAsyncThunk("posts/removePost", async (post) => {
        return await fetch(`/api/posts/remove/${post.id}`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify(post),
        }).then((res) => res.json())});   
        export const addOnePost = createAsyncThunk("posts/addOnePost", async (newPost) => {
            return await fetch(`/api/posts/league/${newPost.leagueId}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json'},
                body: JSON.stringify(newPost),
            }).then((res) => res.json())});
            
    const postSlice = createSlice({
        name: "posts",
        initialState: {
            posts: [],
            status: null,
        },
        dispatch: useDispatch(),
        reducers: {
            addOneLeaguePost: (state, { payload }) => (
                state.posts.push( payload )
            ),
            removeLeaguePost: (state, { payload }) => (
                state.posts = state.posts.filter((post) => post.id !== action.payload.id)
            ),
            getLeaguePosts: (state, { payload }) => (
                state.posts = payload.map(post=> post) 
            ),
            clearState: (state) => (
                state.posts = []
            ),
        },
        extraReducers: {
            [getPosts.pending]: (state) => {
                state.status = "loading"
            },
            [getPosts.resolved]: (state, { payload }) => {
                state.status = "success";
                state.posts = payload.map(post=> post)
            },
            [getPosts.rejected]: (state, action) => {
                state.status = "failed"
            },
            [removePost.pending]: (state) => {
                state.status = "loading"
            },
            [removePost.resolved]: (state, { payload }) => {
                state.status = "success";
                // state.posts.filter((post) => post.id !== payload.id)
                dispatch
            },
            [removePost.rejected]: (state, action) => {
                state.status = "failed"
            },
            [addOnePost.pending]: (state) => {
                state.status = "loading"
            },
            [addOnePost.resolved]: (state, { payload }) => {
                state.status = "success";
                state.posts.push(payload)
            },
            [addOnePost.rejected]: (state, action) => {
                state.status = "failed"
            }
                
        },      
})      




export const { useTheForce } = postSlice.actions

export const selectPosts = ({ posts }) => posts

export default postSlice.reducers


// export commentSlice.reducers as commentReducer
