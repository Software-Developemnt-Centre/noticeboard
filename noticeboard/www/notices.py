import frappe

def get_context(context):
    # Fetch the agent information
    context.name = 'YourAgentName'
    context.car = 'YourCarDetails'

    # Fetch a specific notice (replace 'holiday' with the actual name of your notice)
    notice_doc = frappe.get_doc('notice', 'holiday')
    owner = frappe.get_doc('User', notice_doc.owner)

    context.doc = {
        'owner': owner.username,
        'creation': notice_doc.creation,
        'title': notice_doc.title,
        'user_image': owner.user_image,
        'route': notice_doc.route,
    }

    # Fetch all notices and sort by creation date
    notices = frappe.get_all('notice', fields=['owner', 'creation', 'title', 'route'], order_by='creation DESC')
    context.notices = []

    for notice in notices:
        owner = frappe.get_doc('User', notice.owner)
        context.notices.append({
            'owner': owner.username,
            'creation': notice.creation,
            'title': notice.title,
            'user_image': owner.user_image,
            'route': notice.route,
        })

    return context

