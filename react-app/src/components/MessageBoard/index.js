import { useSelector, useDispatch } from "react-redux"
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import { addOnePost } from "../../store/slices/Postslice"
// import { selectComments } from "../../store/slices/CommentSlice"
import { IconButton, Button, Modal, Form } from 'rsuite';
import { Posts } from "../../store/slices/Posts"

// import ()


export default function MessageBoard() {

    // const posts = useSelector(selectPosts)
    // const comments = useSelector(selectComments)
    const user = useSelector(state => state.session.user)
    const { leagueId } = useParams()
    const [openModal, setOpenModal] = useState(false)
    
    
    const dispatch = useDispatch()
    const [completed, setCompleted] = useState(false)

    const handleOnSubmit = () => {
        return
    }

    useEffect( () => {
    
        if (completed){
            dispatch(addOnePost(FormData))
            setCompleted(false)
        }
    }, [dispatch, completed])


    return (
        <>
            <Posts />
            <Button Primary={true} color='violet' size='lg' onClick={() => setOpenModal(true)}>New Post</Button>
            <Modal backdrop={true} size='lg' show={openModal} onClose={() => setOpenModal(false)}>
                <Form model='' onSubmit={handleOnSubmit}>
                    <Modal.Title><input id="title" value={Form.title} ></input></Modal.Title>
                    {/* <input type="hidden" id="csrf_token" value={csrf_token} /> */}
                    <input type="hidden" id="leagueId" value={leagueId} />
                    <input type="hidden" id="userId" value={user ? user.id : null} />
                    <Modal.Body><IconButton icon={<icon icon={'upload'} />} /><textarea id="body" value={Form.body} ></textarea></Modal.Body>
                    <Modal.Footer><Button block={true} color='green' appearance='primary' onClick={() => setCompleted(true)}>Post to Board</Button></Modal.Footer>
                </Form>
            </Modal>
        </>
    )
}