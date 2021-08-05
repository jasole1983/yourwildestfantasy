import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

export const fetchPostComments = createAsyncThunk(
    "comments/getComments", async (dispatch, getState) => {
        return await fetch("/api/posts/:leagueId/comments/:postId").then(
            (res) => res.json()
        );

    }
);

export const commentSlice = createSlice({
    name: "comments",
    initialState: {
        comments: [],
        status: null,
    },
    reducers: {
        addOnePostComment: (state, action) => {
            state.comments.push(action.payload)
        },
        removePostComment: (state, action) => {
            state.comments.filter((comment)=> comment.id !== action.payload.id)
        },
        getPostComments: (state, action) => {
            state.comments = action.payload 
        },
    },
    extraReducers: {
        [fetchPostComments.pending]: (state) => {
            state.stat = "Loading" 
        },
        [fetchPostComments.resolved]: (state, action) => {
            state.stat = "Success";
            state.comments = action.payload
        },
        [fetchPostComments.rejected]: (state, action) => {
            state.stat = "Failed"
            
        }
    }
    // dispatch(fetchPostComments())
})
export const { addOnePostComment, removePostComment, getPostComments, clearComState } = commentSlice.actions

export default commentSlice.reducer


