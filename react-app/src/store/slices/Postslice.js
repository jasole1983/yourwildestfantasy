import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

export const getPosts = createAsyncThunk(
    "posts/getPosts", async () => {
        return await fetch("/api/posts/").then((res) => res.json());
    }
);
export const removePost = createAsyncThunk(
    "posts/removePost", async (post) => {
        returm await fetch(`/api/posts/remove/${post.id}`, {
                                    method: 'DELETE',
                                    headers: { 'Content-Type': 'application/json'},
                                    body: JSON.stringify(post),
                                    }).then((res) => res.json())});
    
export const     async () => {
        return await fetch()
    }
    )
export const addOnePost = createAsyncThunk(=> (
        state.posts.push(action.payload)
        )
    
    const postSlice = createSlice({
        name: "posts",
        initialState: {
            posts: [],
            status: null,
        },
        reducers: {
                clearState: (state) => (
                    state = {}
                    ),
                },
                extraReducers: {
                    [fetchLeaguePosts.pending]: (state) => {
                        state.status = "loading"
                    },
                    [fetchLeaguePosts.resolved]: (state, action) => {
                        state.status = "success";
                        state.posts = action.payload.map(post=> post)
                    },
                    [fetchLeaguePosts.rejected]: (state, action) => {
                        state.status = "failed"
                    }
                    state.posts.filter((post) => post.id !== payload.id)
                },
        
    // dispatch(fetchLeaguePosts())
})      




export const { addOneLeaguePost, removeLeaguePost, getLeaguePosts, clearState } = postSlice.actions

export const selectPosts = ({ posts }) => posts

export default postSlice.reducers


// export commentSlice.reducers as commentReducer
