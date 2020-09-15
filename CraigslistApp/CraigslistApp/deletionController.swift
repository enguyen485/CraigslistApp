//
//  deletionController.swift
//  
//
//  Created by Eric Nguyen on 9/13/20.
//

import UIKit

class deletionController: UIViewController {

    var contact: Int?
    var hyperlink: String?
    var urls = [(String)]()
    
    @IBOutlet weak var hyperlinkLabel: UILabel!
    @IBOutlet weak var deleteButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        hyperlinkLabel.text = hyperlink
    }
    

    @IBAction func onClick(_ sender: Any) {
        APIHandler.deleteUrl(id: contact!)
    }
    

}
