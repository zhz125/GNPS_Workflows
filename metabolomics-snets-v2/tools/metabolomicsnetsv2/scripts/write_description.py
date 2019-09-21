import sys
import os
import proteosafe


param_obj = proteosafe.parse_xml_file(sys.argv[1])
output_filename = sys.argv[2]

output_sentences = []
output_sentences.append("<strong>Classical Molecular Networking Workflow Description</strong><br><br>\n\n")
output_sentences.append("A molecular network was created using the online workflow (https://ccms-ucsd.github.io/GNPSDocumentation/) on the GNPS website (http://gnps.ucsd.edu).")
if param_obj["FILTER_PRECURSOR_WINDOW"][0] == "1":
    output_sentences.append("The data was filtered by removing all MS/MS fragment ions within +/- 17 Da of the precursor m/z.")
if param_obj["WINDOW_FILTER"][0] == "1":
    output_sentences.append("MS/MS spectra were window filtered by choosing only the top 6 fragment ions in the +/- 50Da window throughout the spectrum.")
if param_obj["RUN_MSCLUSTER"] == "on":
    output_sentences.append("The data was then clustered with MS-Cluster with a parent mass tolerance of " +
                                                    param_obj["tolerance.PM_tolerance"][0] + " Da and a MS/MS fragment ion tolerance of " + param_obj["tolerance.Ion_tolerance"][0] +
                                                    " Da to create consensus spectra . Further, concensus spectra that contained less than " + param_obj["CLUSTER_MIN_SIZE"][0] + " spectra" +
                                                    " were discarded.")

output_sentences.append("The precursor ion mass tolerance was set to %s Da and a MS/MS fragment ion tolerance of %s Da." % (param_obj["tolerance.PM_tolerance"][0], param_obj["tolerance.Ion_tolerance"][0]))
output_sentences.append("A network was then created where edges were filtered to have a cosine score above %s and more than %s matched peaks." % (param_obj["PAIRS_MIN_COSINE"][0], param_obj["MIN_MATCHED_PEAKS"][0]))
output_sentences.append("Further, edges between two nodes were kept in the network if and only if each of the nodes appeared in each other's respective top %s most similar nodes." % (param_obj["TOPK"][0]))
output_sentences.append("Finally, the maximum size of a molecular family was set to %s, and the lowest scoring edges were removed from molecular families until the molecular family size was below this threshold." % (param_obj["MAXIMUM_COMPONENT_SIZE"][0]))
output_sentences.append("The spectra in the network were then searched against GNPS' spectral libraries.")
if param_obj["FILTER_LIBRARY"][0] == "1":
    output_sentences.append("The library spectra were filtered in the same manner as the input data.")
output_sentences.append("All matches kept between network spectra and library spectra were required to have a score above %s and at least %s matched peaks." % (param_obj["SCORE_THRESHOLD"][0], param_obj["MIN_MATCHED_PEAKS_SEARCH"][0]))
output_sentences.append("<br><br>\n<strong>Citation</strong><br><br>\n")
output_sentences.append('Wang, Mingxun, et al. "Sharing and community curation of mass spectrometry data with Global Natural Products Social Molecular Networking." Nature Biotechnology 34.8 (2016): 828-837. PMID: 27504778, https://www.nature.com/articles/nbt.3597')
output_sentences.append('<br><br>')

if param_obj["RUN_MSCLUSTER"] == "on":
    output_sentences.append('Frank, Ari M., et al. "Clustering millions of tandem mass spectra." Journal of proteome research 7.01 (2007): 113-122. PMID: 18067247, https://pubs.acs.org/doi/abs/10.1021/pr070361e')


open(output_filename, "w").write(" ".join(output_sentences))
