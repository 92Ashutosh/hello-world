def vendor_agent(vendor):

    approved_vendors = ["Dell", "Lenovo", "HP"]

    if vendor in approved_vendors:
        return "Approved Vendor"
    else:
        return "Unapproved Vendor"