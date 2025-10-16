def generate_report(original, reconstructed, links):
    report = "---  RECONSTRUCTION REPORT --- \n\n"
    report += "[Original Fragment]\n" + f"> {original}\n\n"
    report += "[AI-Reconstructed Text]\n" + f"> {reconstructed}\n\n"
    report += "[Contextual Sources]\n"
    if links:
         for link in links:
             report += f"* {link}\n"
    else:
        report += "No contextual sources found\n"
    
    return report
