import { useSelector, useDispatch } from "react-redux"
import { useEffect } from "react"
// import { useParams } from "react-router-dom"
import { fetchLeaguePosts, selectPosts } from "../../store/slices/Postslice"
import { selectComments, fetchPostComments  } from "../../store/slices/CommentSlice"
import { List, Button } from 'rsuite';
import ()


export default function MessageBoard() {

    const posts = useSelector(selectPosts)
    const comments = useSelector(selectComments)
    // const { leagueId } = useParams()
    
    const dispatch = useDispatch()
    useEffect( () => {
        dispatch(fetchLeaguePosts())
        dispatch(fetchPostComments())
    }, [])


    return (
        <>
            <List border={true} hover={true} className="post_list_cont">
                {posts && posts.map((post, i) => (
                    <List.Item index={i} className={`post_list_item_${i}`}>
                    <h5>{post.title}</h5>
                    <div className="post_btn_cont">
                        <Button size="small" className={`delbtn_${i}`}>X</Button>
                        <Button size="small" className={`edit_${i}`}>. . .</Button>
                    </div>
                    <p className={`body${i}`}>{post.body}</p>
                    <List border={true} hover={true} className="comm_list_cont">
                        { comments && comments.map((comment, j) => (
                        <List.Item index={j} className={`post_comm_list_${j}`} >
                        <div className="comm_btn_cont">
                            <Button size="small" className={`com_delbtn_${j}`}>X</Button>
                            <Button size="small" className={`com_edit_${j}`}>. . .</Button>
                        </div>
                        <p className={`com_body${j}`}>{comment.body}</p>
                        </List.Item>
                        ))}
                    </List>
                    </List.Item>
                ))} 
            </List>
            <Button Primary={true} color='violet' size='large'>New Post</Button>
        </>
    )
}