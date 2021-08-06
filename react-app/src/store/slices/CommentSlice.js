import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

export const getComments = createAsyncThunk("comments/getComments", async () => {
        return await fetch("/api/comments/").then((res) => res.json())});
    

export const removeComment = createAsyncThunk("comments/removeComment", async (comment) => {
        return await fetch(`/api/comments/remove/${comment.id}`, {
                                    method: 'DELETE',
                                    headers: { 'Content-Type': 'application/json'},
                                    body: JSON.stringify(comment),
                                    }).then((res) => res.json())});   
export const addOneComment = createAsyncThunk("comments/addOneComment", async (newComment) => {
        return await fetch(`/api/comments/${newComment.postId}/create`, {
                                    method: 'POST',
                                    headers: { 'Content-Type': 'application/json'},
                                    body: JSON.stringify(newComment),
                                    }).then((res) => res.json())});
    
    const commentSlice = createSlice({
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
        
            rhubGold: ((state) => {
               const newState = [...state.comments] 
                return state = { comments: newState }
            })
        },
        extraReducers: {
            [getComments.pending]: (state) => {
                state.status = "loading"
            },
            [getComments.resolved]: (state, { payload }) => {
                state.status = "success";
                state.comments = payload.map(comment=> comment)
            },
            [getComments.rejected]: (state, action) => {
                state.status = "failed"
            },
            [removeComment.pending]: (state) => {
                state.status = "loading"
            },
            [removeComment.resolved]: (state, { payload }) => {
                state.status = "success";
                state.comments.filter((comment) => comment.id !== payload.id)
            },
            [removeComment.rejected]: (state, action) => {
                state.status = "failed"
            },
            [addOneComment.pending]: (state) => {
                state.status = "loading"
            },
            [addOneComment.resolved]: (state, { payload }) => {
                state.status = "success";
                state.comments.push(payload)
            },
            [addOneComment.rejected]: (state, action) => {
                state.status = "failed"
            }
                
        },      
})      




export const { rhubGold } = commentSlice.actions

export const selectComments = ({ comments }) => comments

export default commentSlice.reducers


// export commentSlice.reducers as commentReducer


